import random
import uuid
from typing import Protocol, OrderedDict

from django.core.cache import cache
from rest_framework_simplejwt import tokens

from . import repos


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> str: ...

    def verify_user(self, data: OrderedDict) -> None: ...

    def create_token(self, data: OrderedDict) -> str: ...

    def verify_token(self, data: OrderedDict) -> dict: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> str:
        code = self._generate_code()
        session_id = str(uuid.uuid4())
        cache.set(session_id, {**data, 'code': code}, timeout=300)
        self._send_sms_to_phone_number(phone_number=data['phone_number'], code=code)

        return session_id

    def verify_user(self, data: OrderedDict) -> None:
        user_data = cache.get(data['session_id'])

        if not user_data:
            return

        if user_data['code'] != data['code']:
            return

        user = self.user_repos.create_user(data={
            'email': user_data['email'],
            'phone_number': user_data['phone_number'],
        })

        self._send_letter_to_email(email=user.email)

    def create_token(self, data: OrderedDict) -> str:
        user = self.user_repos.get_user(data=data)
        code = self._generate_code()
        session_id = str(uuid.uuid4())
        cache.set(session_id, {'phone_number': str(user.phone_number), 'code': code}, timeout=300)
        self._send_sms_to_phone_number(phone_number=data['phone_number'], code=code)

        return session_id

    def verify_token(self, data: OrderedDict) -> dict:
        user_data = cache.get(data['session_id'])

        if not user_data:
            return

        if user_data['code'] != data['code']:
            return

        user = self.user_repos.get_user(data={'phone_number': user_data['phone_number']})

        access = tokens.AccessToken.for_user(user)
        refresh = tokens.RefreshToken.for_user(user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }

    @staticmethod
    def _send_letter_to_email(email: str) -> None:
        print(f'send letter to {email}')

    @staticmethod
    def _send_sms_to_phone_number(phone_number: str, code: str) -> None:
        print(f'send sms code {code} to {phone_number}')

    @staticmethod
    def _generate_code() -> str:
        return ''.join(random.choices([str(i) for i in range(10)], k=4))
