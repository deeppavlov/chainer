from deeppavlov.testing.test_case import DPTestCase
from deeppavlov.core.components import read_configuration, init_component
from deeppavlov.core.vocab import VocabComponent
import deeppavlov.ner
import os


class TestTrain(DPTestCase):

    def test_tokens_vocab_train(self):
        cfg = read_configuration("./conf/train.vocab.tokens.json")
        cmp = init_component(cfg)
        cmp.train({})
        cmp.save()
        assert os.path.exists("./tmp/vocabs/ner.tokens.vocab.txt")
        tc = cmp.get_trained_component()
        assert isinstance(tc, VocabComponent)
        assert 441 == len(tc.vocab._t2i)

    def test_tags_vocab_train(self):
        cfg = read_configuration("./conf/train.vocab.tags.json")
        cmp = init_component(cfg)
        cmp.train({})
        cmp.save()
        assert os.path.exists("./tmp/vocabs/ner.tags.vocab.txt")
        tc = cmp.get_trained_component()
        assert isinstance(tc, VocabComponent)
        assert 11 == len(tc.vocab._t2i)

    def test_chars_vocab_train(self):
        cfg = read_configuration("./conf/train.vocab.chars.json")
        cmp = init_component(cfg)
        cmp.train({})
        cmp.save()
        assert os.path.exists("./tmp/vocabs/ner.chars.vocab.txt")
        tc = cmp.get_trained_component()
        assert isinstance(tc, VocabComponent)
        assert 26 == len(tc.vocab._t2i)

    def test_ner_train(self):
        cfg = read_configuration("./conf/train.ner.json")
        cmp = init_component(cfg)
        cmp.train({})
        cmp.save()
        assert os.path.exists("./tmp/models/ner.index")
        assert os.path.exists("./tmp/models/ner.meta")
        assert os.path.exists("./tmp/models/checkpoint")
