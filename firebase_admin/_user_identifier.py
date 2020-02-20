# Copyright 2020 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Classes to uniquely identify a user."""

class UserIdentifier:
    """Identifies a user to be looked up."""


class UidIdentifier(UserIdentifier):
    """Used for looking up an account by uid.

    See ``auth.get_user()``.
    """

    def __init__(self, uid):
        """Constructs a new `UidIdentifier` object.

        Args:
            uid: A user ID string.
        """
        self.uid = uid


class EmailIdentifier(UserIdentifier):
    """Used for looking up an account by email.

    See ``auth.get_user()``.
    """

    def __init__(self, email):
        """Constructs a new `EmailIdentifier` object.

        Args:
            email: A user email address string.
        """
        self.email = email


class PhoneIdentifier(UserIdentifier):
    """Used for looking up an account by phone number.

    See ``auth.get_user()``.
    """

    def __init__(self, phone_number):
        """Constructs a new `PhoneIdentifier` object.

        Args:
            phone_number: A phone number string.
        """
        self.phone_number = phone_number


class ProviderIdentifier(UserIdentifier):
    """Used for looking up an account by provider.

    See ``auth.get_user()``.
    """

    def __init__(self, provider_id, provider_uid):
        """Constructs a new `ProviderIdentifier` object.

        Args:
            provider_id: A provider ID string.
            provider_uid: A provider UID string.
        """
        self.provider_id = provider_id
        self.provider_uid = provider_uid
