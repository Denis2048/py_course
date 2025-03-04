import pytest
from mobile_phone import MobilePhone

@pytest.fixture
def mobile_phone_off():
    """Фикстура с выключенным телефоном."""
    return MobilePhone("123-456-789")

@pytest.fixture
def mobile_phone_on():
    """Фикстура с включенным телефоном."""
    phone = MobilePhone("123-456-789")
    phone.turn_on()
    return phone

def test_turn_on(mobile_phone_off):
    """Тест для проверки включения телефона."""
    assert mobile_phone_off.switch == False
    result = mobile_phone_off.turn_on()
    assert result == "\nТелефон включен"
    assert mobile_phone_off.switch == True

def test_turn_off(mobile_phone_on):
    """Тест для проверки выключения телефона."""
    assert mobile_phone_on.switch == True
    result = mobile_phone_on.turn_off()
    assert result == "\nТелефон выключен"
    assert mobile_phone_on.switch == False

def test_call_when_phone_is_on(mobile_phone_on):
    """Тест для проверки звонка с включенного телефона."""
    result = mobile_phone_on.call("123-456-789")
    assert result == "\nЗвонок на 123-456-789 ...."

def test_call_when_phone_is_off(mobile_phone_off):
    """Тест для проверки звонка с выключенного телефона."""
    result = mobile_phone_off.call("123-456-789")
    assert result == "\nТелефон 123-456-789 выключен, нельзя позвонить"
