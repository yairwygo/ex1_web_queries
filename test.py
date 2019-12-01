from Dictionary import *
from PostingList import *
def prRed(x): print("\033[91m {}\033[00m".format(x))
def prGreen(x): print("\033[92m {}\033[00m".format(x))
def prBlue(x): print("\033[34m {}\033[00m".format(x), end=" ")
def prYellow(x): print("\033[93m {}\033[00m".format(x))

POST_DEBUG = True
DICT_DEBUG = True
if DICT_DEBUG:
    # Define initial data
    prYellow("Initializing tests data")
    STR = ('STR')
    BLK = ('BLK', 4)
    FC = ('FC', 4)
    terms = ['ba', 'banana', 'car', 'cat', 'dog', 'doggy', 'dump', 'far', 'formula', 'in', 'input', 'int']


    # Test STR
    prYellow('Testing STR...')
    try:
        prBlue('Creating STR Dictionary...')
        STR_dictionary = Dictionary(terms, STR)
        prGreen('OK!')
    except:
        prRed('Failed')
        '''
            try:
        prBlue('Validating Stored info...')
        assert (STR_dictionary.term_info == [(0, 'SOME DOCS'), (2, 'SOME DOCS'), (8, 'SOME DOCS'), (11, 'SOME DOCS'), (14, 'SOME DOCS'), (17, 'SOME DOCS'),
                                         (22, 'SOME DOCS'), (26, 'SOME DOCS'), (29, 'SOME DOCS'), (36, 'SOME DOCS'), (38, 'SOME DOCS'), (43, 'SOME DOCS')])
        prGreen('OK!')
    except:
        prRed('Failed')
        '''

    try:
        prBlue('Validating GetString...')
        assert (STR_dictionary.GetString() == 'babananacarcatdogdoggydumpfarformulaininputint')
        prGreen('OK!')
    except:
        prRed('Failed')
    try:
        prBlue('Validating GetInfo...')
        assert (STR_dictionary.GetInfo('doggy') == 17)
        prGreen('OK!')
    except:
        prRed('Failed')
    try:
        prBlue('Validating GetInfo (Non-existent term)...')
        assert (STR_dictionary.GetInfo('baba') is None)
        prGreen('OK!')
    except:
        prRed('Failed')


    # Test BLK
    prYellow('Testing BLK...')
    try:
        prBlue('Creating BLK Dictionary...')
        BLK_dictionary = Dictionary(terms, BLK)
        prGreen('OK!')
    except:
        prRed('Failed')
        '''
            try:
        prBlue('Validating Stored info...')
        assert (BLK_dictionary.term_info == [(2, 'SOME DOCS', 0), (6, 'SOME DOCS'), (3, 'SOME DOCS'), (3, 'SOME DOCS'), (3, 'SOME DOCS', 14), (5, 'SOME DOCS'),
                                             (4, 'SOME DOCS'), (3, 'SOME DOCS'), (7, 'SOME DOCS', 29), (2, 'SOME DOCS'), (5, 'SOME DOCS'), (3, 'SOME DOCS')])
        prGreen('OK!')
    except:
        prRed('Failed')
        '''

    try:
        prBlue('Validating GetString...')
        #bananacartdoggyumpfarformulainputt
        #assert (BLK_dictionary.GetString() == 'babananacarcatdogdoggydumpfarformulaininputint')

        assert (BLK_dictionary.GetString() == 'babananacarcatdogdoggydumpfarformulaininputint')
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating GetInfo...')
        assert (BLK_dictionary.GetInfo('doggy') == (14, 3, 5, 4, 3))
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating GetInfo (Non-existent term)...')
        assert (BLK_dictionary.GetInfo('baba') is None)
        prGreen('OK!')
    except:
        prRed('Failed')

    # Test FC
    prYellow('Testing FC...')

    try:
        prBlue('Creating FC Dictionary...')
        FC_dictionary = Dictionary(terms, FC)
        prGreen('OK!')
    except:
        prRed('Failed')

    '''
        try:
        prBlue('Validating Stored info...')
        assert (FC_dictionary.term_info == [(2, 'SOME DOCS', 0, 0), (6, 'SOME DOCS', 2), (3, 'SOME DOCS', 0), (3, 'SOME DOCS', 2), (3, 'SOME DOCS', 0, 10), (5, 'SOME DOCS', 3),
                                             (4, 'SOME DOCS', 1), (3, 'SOME DOCS', 0), (7, 'SOME DOCS', 0, 21), (2, 'SOME DOCS', 0), (5, 'SOME DOCS', 2), (3, 'SOME DOCS', 2)])
        prGreen('OK!')
    except:
        prRed('Failed')
    '''


    try:
        prBlue('Validating GetString...')
        assert (FC_dictionary.GetString() == 'bananacartdoggyumpfarformulainputt')
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating GetInfo...')
        assert (FC_dictionary.GetInfo('doggy') == (10, (3, 0), (5, 3), (4, 1), (3, 0)))
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating GetInfo (Non-existent term)...')
        assert (FC_dictionary.GetInfo('baba') is None)
        prGreen('OK!')
    except:
        prRed('Failed')

if POST_DEBUG:
    docIDs = [7, 12, 23, 1033, 2354634, 2354636]
    prYellow('Testing Posting Lists...')
    try:
        prBlue('Creating V List...')
        posting_list = PostingList(docIDs, 'V')
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating V GetInfo...')
        assert(posting_list.GetList() == bytearray(b'\x87\x85\x8b\x07\xf2\x01\x0fS\xc1\x82'))
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Creating LP List...')
        posting_list = PostingList(docIDs, 'LP')
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating LP GetInfo...')
        assert(posting_list.GetList() == bytearray(b'\x07\x05\x0bC\xf2\xa3\xe9\xc1\x02'))
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Creating GV List...')
        posting_list = PostingList(docIDs, 'LP')
        prGreen('OK!')
    except:
        prRed('Failed')

    try:
        prBlue('Validating GV GetInfo...')
        assert(posting_list.GetList() == bytearray(b'\x07\x05\x0bC\xf2\xa3\xe9\xc1\x02'))
        prGreen('OK!')
    except:
        prRed('Failed')


