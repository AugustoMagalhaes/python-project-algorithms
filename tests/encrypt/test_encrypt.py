import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    invalid_key = encrypt_message("ABCD", 20)
    assert invalid_key == "DCBA"

    odd_key_valid = encrypt_message("ABCD", 3)
    assert odd_key_valid == "CBA_D"

    even_key_valid = encrypt_message("ABCD", 2)
    assert even_key_valid == "DC_BA"

    with pytest.raises(TypeError) as e_message:
        encrypt_message([], 1)
    assert "tipo inválido para message" in e_message.value.args

    with pytest.raises(TypeError) as e_key:
        encrypt_message("ABCD", [])
    assert "tipo inválido para key" in e_key.value.args
