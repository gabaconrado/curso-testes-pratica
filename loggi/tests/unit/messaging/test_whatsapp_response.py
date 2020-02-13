import pytest

from mock import MagicMock
from messaging.helpers.twillio import whatsapp_rating_reply_message

"""
According to our specification, our valid equivalence classes are:
    - Response BOA
    - Response RUIM
    - Invalid
"""



GOOD_MSG_TMPL =  ('Que bom, %s. Ficamos felizes que a sua experiência tenha sido boa.\n\n'
                  'Obrigada por nos ajudar, respondendo à pesquisa. :blue_heart:')


BAD_MSG_TMPL = ('Poxa, %s, a gente sente muito que a experiência de ligação não tenha sido boa.\n\n'
                'Vamos trabalhar por aqui para melhorar esse ponto.\n\n'
                'Obrigada por nos ajudar, respondendo à pesquisa. :blue_heart:')

INVALID_MSG_TMPL = ('Eita, a gente não conseguiu entender a sua resposta. :thinking_face:\n\n'
                    'Digite *BOA*, se correu tudo bem durante a ligação.\n\n'
                    'Ou mande *RUIM*, se você não teve uma boa experiência.\n\n'
                    '---\n' \
                    ':point_right:Essa é uma mensagem automática. '
                    'Para nos contar sua experiência, é preciso digitar uma das duas palavras '
                    'que estão acima em negrito.')

VALID_INTENTION = 'driver_incident.driver_call_rating'

NAME = 'Neymar'

@pytest.mark.parametrize(
    'response, intention, expected',
    [
        ('BOA', VALID_INTENTION, GOOD_MSG_TMPL %  NAME),
        ('RUIM', VALID_INTENTION, BAD_MSG_TMPL % NAME),
        ('BLABLA', VALID_INTENTION, INVALID_MSG_TMPL),
        ('BOA' 'blabla', VALID_INTENTION, INVALID_MSG_TMPL)
    ],
    ids = [
        'Boa',
        'Ruim',
        'Msg inválida',
        'Intenção inválida'
    ]
)
def test_whatsapp_reply(response, intention, expected):
    recipient = MagicMock(first_name=NAME)
    assert whatsapp_rating_reply_message(intention, response, recipient) == expected