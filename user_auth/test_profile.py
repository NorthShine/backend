import pytest

from user_auth.models import Profile
from competitions.models import Competency
from user_auth.serializers import ProfileSerializer

from django.conf import settings
from hack_backend import settings


def pytest_configure():
    settings.configure(DATABASES=settings.DATABASES)


def prepare_data():
    my_user = Profile.objects.get(username='test_user')
    jun_backend = Competency.objects.get(name='Junior Backend')
    my_user.competencies.add(jun_backend)
    return my_user, jun_backend

# test there is no exception raised
@pytest.mark.django_db
def test_user_serialization():
    my_user, jun_backend = prepare_data()
    serializer = ProfileSerializer(instance=my_user)
    print(serializer.data)


@pytest.mark.django_db
def test_profile_serialization():
    my_user, jun_backend = prepare_data()
    serializer = ProfileSerializer(instance=my_user)
    serialized = serializer.data

    expected_data = {
        'email': 'test_mail@fakedomain.kuk',
        'role': 'EMPLOYEE',
        'username': 'test_user',
        'competencies': [
            {'name': 'Junior Backend',
             'level': 1,
             'user': 2}]}

    assert expected_data == serialized
