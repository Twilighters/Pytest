import pytest
import os
from main import email_check
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize("email_data", ["testi@testi.ru", "wix@wix.com", "123QWE@mmm.mmm"])
def test_email(email_data):
    LOGGER.info(email_data)
    assert email_check(email_data) is True


@pytest.mark.parametrize("email_data", ["testi@testi.", "wix@", "@tt"])
def test_email_invalid(email_data):
    LOGGER.info(email_data)
    assert email_check(email_data) is False
