

import time


vocab =['c', 'a', 'T', 'D', 'i', 'G', 's', 'M', 'b', 'F', 'n', 'O', 'g', 'o', "'", 'H', 'A', '$', 'u', '.', 'S', 'Q', '&', 'Y', 'I', '!', 'W', 'V', 'E', 'U', ';', 'v', 'x', 'k', 'L', 'j', 'l', 'w', 'K', 'J', 'z', 'f', 'R', 'y', 'e', '\n', 'h', 'r', ',', '?', 'Z', 'X', 'm', 'B', '-', 'C', 't', 'd', '3', 'N', 'q', 'P', ' ', 'p', ':', 'th', 'he', 'ou', 'er', 'in', 'the', 'an', 're', 'ha', 'nd', 'or', 'at', 'en', 'is', 'ar', 'hi', 'st', 'es', 'on', 'll', 'ea', 'me', 'it', 've', 'to', 'se', 'ur', 'no', 'ho', 'ng', 'and', 'yo', 'you', 'te', 'le', 'al', 'ot', 'ow', 'be', 'ne', 'as', 'wi', 'e,', 'of', 'ee', 'nt', 'ed', 'ing', 'om', 'ro', 'el', 'de', 'our', 'lo', 'ce', 'ma', 'fo', 'us', 'sh', 'co', 'ch', 'il', 'et', 'Th', 'ri', 'we', 'ti', 'my', 'ut', 'so', 'li', 'ir', 'rd', 'rs', 'oo', 'ra', 'ay', 'tha', 'av', 'ith', 's,', 'ld', 'ke', 'ai', 'la', 'rt', 'for', 'ie', 'wh', 'ul', 'thi', 'un', 'not', 'ad', 'im', 'An', 'her', "'s", 'si', 'wa', 'hat', 'gh', 'do', 'ther', 'nc', 'd,', 'ic', 'that', 'pe', 'ta', 't,', 'ge', 'And', 'wo', 'tr', 'ss', 'mo', 'Wh', 'tho', 'with', 'am', 'ill', 'di', 'pr', 'em', 'his', 'od', 'ns', 'y,', 'ol', 'ent', 'e.', 'your', 'thou', 'ca', 'ac', 'ter', 'hy', 'io', 'os', 'ak', 'r,', 'ome', 'fa', 'ath', 'ig', 'O:', 'fe', 'mi', 'id', "'d", 'po', 'go', 'ly', 'ere', 'ear', 'hav', 'all', 'ht', 'ds', 'EN', 'sa', 'n,', 'ght', 'ord', 'The', 'have', 'oul', 'bu', 'oth', 'are', 'him', 'ei', 'IN', 'su', 'bl', 'this', 'IO', 'pa', 'ov', 'ec', 'ell', 'S:', 'ry', 'if', 'iv', 'hea', 'ore', 'br', 'ver', 'sp', 'gr', 'ain', 'AR', 'man', 'fr', 'ould', 'here', 'ev', 'thy', 'ck', 'bo', 'sha', 'one', 'now', 'ess', 'ue', 'hal', 'IO:', 'ey', 'est', 'ki', 'uc', 'will', 'ts', 'rea', 'da', 'ni', 'hou', 'fi', 'vi', 'ty', 'ag', 'ru', 'but', 'ep', 'ug', 'ous', 's.', 'pl', 'ef', 'To', 'US', 'rr', 'US:', 'hall', 't.', 'tt', 'thin', 'res', 'na', 'kin', 'ion', 'wn', 'tl', 'ba', 'up', 'art', 'by', 'RI', 'ine', 'end', 'thee', 'oun', 'ard', 'ga', 'NG', 'wor', 'au', 'ood', 'ye', 'rn', 'ast', 'hen', 'tu', 'e:', 'wer', 'shall', 'mu', 'e;', 'He', 'kn', 'ers', 'ive', 'ove', 'No', 'me,', 'o,', 'UC', 'd.', 'ap', 'ING', 'er,', 'rom', "e'", 'men', 'AN', 'CE', 'ust', 'sel', 'han', 'lor', 'That', 'Tha', 'ct', 'Bu', 'Yo', 'wha', 'ER', 'own', 'what', 'OR', 'ci', 'hear', 'l,', 'ant', 'h,', 'nk', 'king', 'ost', 'pi', 'LA', 'ew', 'op', 'der', 'com', 'ff', 'she', 'ate', 'ok', "'l", 'ET', 'goo', 'ven', 'ES', 'igh', 'con', 'ls', 'r.', 'LI', 'cr', 'qu', 'But', "r'", 'n.', 'oug', 'mp', 'sw', 'ough', 'ab', 'RD', 'cou', 'hu', 'gi', 'ble', 'row', 'war', 'hic', "'t", 'hich', 'n:', 'lt', 'lf', 'good', "'ll", 'whe', 'ind', 'A:', 'TI', 'aw', 'Wha', 'min', 'was', 'fu', 'What', 'y.', 'rin', 'LO', 'You', 'KIN', 'wou', 'KING', 'KI', 'ose', 'Fo', 'ia', 'come', 'e?', 'CH', 'ong', 'kno', 'rm', 'ik', 'NI', 'from', 'dr', 'HA', 'les', 'rc', 'anc', 'more', 'Go', 'well', 'them', 'NT', 'For', 'rth', 'loo', 'IC', 'uch', 'can', 'dea', 'out', 'ort', 'sir', 'tle', 'TE', 'self', 'OL', 'sin', 'cu', 'would', "n'", 'know', 'per', 'ure', 't:', 'r:', 's;', 'love', 'whi', 'ys', 'es,', 'ran', 'Co', 'pea', 'ny', 'int', 'een', 'sc', 'EL', 'lea', 'um', 'see', 'dy', 'say', 'let', 'Ma', 'We', 'then', "I'", 'IU', 's:', 'mak', 'IUS:', 'rl', 'ARD', 'son', 'oi', 'ond', 'rou', 'mb', 'their', 'thei', 'm,', 'than', 'u,', 'hr', 'pp', 'My', 'cl', 'ame', 'there', 'ins', 'e!', 'ME', 'ou,', 'enc', 'how', 'gu', '--', 'they', 'ce,', 'Wi', 'ST', 'ake', 'Ha', 'fore', 'str', 'pu', 'lan', 'ave', "I'll", 'lik', 'ay,', 'tre', 'sl', 'pre', 'NC', 'E:', 'pon', "er'", 'tin', 'ui', 'rv', 'rie', 'ist', 'sen', 'w,', 'Se', 'ink', 'ON', 'rst', 'inc', 'd;', 'ft', 'RO', 'par', 'nn', 'may', 'rse', 'ish', 'k,', 'other', 'KE', 'bro', 'way', 'pro', 'As', 'har', 'ms', 'oy', "t'", 'ves', 'ir,', 'Whe', 'ang', 'd:', 'll,', 'eo', 'bi', 'T:', 'vo', 'ars', 'rk', 'tw', 'any', 'gain', 'ies', 'hath', 'nou', 'who', 'ob', 'were', 'eak', 'erv', 'lin', 'tor', 'ws', 'ons', 'II', 'oc', 'eg', 'ors', 'nes', 'ery', 'ather', 'dis', 'du', 'thing', 'ud', 'irst', 'g,', 'ks', 'llo', 'like', 'ted', 'cha', 'Lo', 'Be', 'on,', 'had', 'arr', 'gen', 'DU', 'gs', 'ace', 'eath', 'ten', 'MI', 'make', 'HAR', 'must', 'va', 'So', 'oa', 'gra', 'RE', 'ound', 'shou', 'rg', 'ight', 'th,', 'you,', 'BE', 'ster', 'fl', 'ati', 'some', 'ise', 'should', 'tan', 'father', 't;', 'Sh', 'tru', 'VI', 'Whi', 'er.', 'TIO:', 'use', 'af', 'PE', 'ity', 'ime', 'I:', 'sti', 'NE', 'too', 're,', 'ser', 'upon', 'hil', 'CA', 'eas', 'Ho', 'ree', 'ET:', 'AU', 'OM', "o'", 'LE', 'air', 'ex', 'reat', 'tc', 'HE', 'day', 'has', 'l.', 'RU', 'des', 'did', 'lord', 'wee', 'thr', 'hon', 'pt', 'which', 'gl', 'gre', 'er:', 'In', 'death', 'LU', 'st,', 'lu', 'gn', 'ful', 'Fi', 'eed', 'IS', 'fri', 'ub', 'lif', 'old', 'ren', 'eth', 'eep', 'If', 'ire', 'spea', 'EO', 'don', 'ing,', 'mis', 'oe', 's!', 's?', 'mes', 'K:', 'roth', 'ip', 'red', 'entle', 'ans', 'time', 'again', 'when', 'che', 'RIC', 'RICH', 'hol', 'iti', 'UK', 'mar', 'hand', 'llow', 'off', 'UKE', 'DUKE', 'R:', 'orn', 'm.', 'yet', 'ze', 'think', 'ray', 'Ro', 'With', 'nf', 'dl', 'r;', 'WA', 'Ca', 'Si', 'ces', 'Thou', 'ein', 'TH', 'UL', 'ger', 'RICHARD', 'sou', 'CHAR', 'CHARD', 'ENT', 'ENTIO:', 'mm', 'CEN', 'WAR', 'ER:', 'ord,', 'Which', 'take', 'ade', 'tis', 'ever', 'IA', 'ved', 'CI', 'ret', 'dow', 'very', 'TER', 'din', 'though', 'ont', 'thes', 'ann', 'Y:', 'orth', 'vin', 'O,', 'n;', 'rother', 'INC', 'nds', 'nder', 'blo', 'LL', 'onou', 'TR', 'ua', 't?', 'speak', 'stan', 'Why', 'inst', 'sir,', 'give', 'ence', 'Of', "l'", 'ugh', 'att', 'such', 'Cl', 'land', 'Le', 'Fir', 'First', 'ance', 'gent', 'ings', 'sta', 'wr', 'ther,', "d'", 'most', 'AB', 'ead', 'tell', 'brother', 'lon', 'ean', 'me.', 'these', 'D:', 'ice', 'heav', 'h.', 've,', 'mer', "'e", 'ward', "s'", 'UE', 'onour', 'where', 'bre', 'rem', 'ste', 'Pr', 'Is', 'iou', 'ban', 'chi', 'tion', 'ass', 'ied', 'ens', 'How', 'ris', 'ower', 'OU', 'orr', 'Her', "t's", 'low', 'new', 'Wa', 'This', 'TER:', 'riend', 'Who', 'EST', 'en,', 'o.', 'sed', 'look', 'RY', 'UCH', 'friend', 'ron', 'LO:', "y'", 'Come', 'que', 'cond', 'ESTER:', 'OUC', 'UCE', 'UCESTER:', 'UCES', 'LOUCESTER:', 'GLO', 'GLOUCESTER:', 'LOUC', 'GL', 'gentle', 'nce', "er's", 'itt', 'y;', 'y:', 'dre', 'ving', 'UT', 'hast', 'EE', 'den', 'EEN', 'urse', 'ber', 'win', 'Lor', 'iu', 'lou', 'eri', 'nob', 'God', 'less', 'yse', 'and,', 'pra', 'eav', 'ner', 'nl', 'lood', 'nd,', 'Rome', 'd?', 'le,', 'ian', 'mor', 'rf', 'CO', 'VIN', 'urn', "'st", 'cc', 'CENTIO:', 'VINC', 'INCENTIO:', 'QUE', 'UEEN', 'VINCENTIO:', 'QUEEN', 'LAN', 'QU', 'fair', 'honour', 'Mar', 'eac', 'bou', 'ount', 'BR', 'ness', 'mon', 'much', "h'", 'OF', 'mine', 'in,', 'nat', 'sto', 'Where', 'ment', 'thee,', 'dee', 'UM', 'lord,', 'uk', 'eet', 'fear', 'blood', 'lie', 'rest', 'jo', 'r?', 'stand', 'ands', 'arm', 'made', 'iz', 'lem', 'AM', 'rac', 'ene', 'g.', 'HEN', "'tis", 'ps', 'Now', 'nor', 'ring', 'se,', 'd!', 'rep', 'bear', 'ju', 'nu', 'thu', 'bet', 'nev', 'Ti', 'Lord', 'ENRY', 'HENRY', 'ow,', 'ENR', 'NR', 'great', 'hel', 'pla', 'rec', 'never', 'f,', 'ien', 'iss', "k'", 'it,', 'read', 't!', 'fort', 'erc', 'anno', 'oin', 'je', 'an:', 'omp', 'ce.', 'ince', 'ph', 'll.', 'lse', 'e-', 'ert', "'T"]
s = "hello"
    

#print(s)
VOCAB = {}
c = 0
for i in vocab:
    VOCAB[i] = c
    c+=1

     

def ENCODE(txt , vocab ):
    print(txt)
    d = []
    lenV = len(txt)
    
    _ = 0
    while _ < lenV:
            if _!=lenV-1 and txt[_]+txt[_+1] in vocab:
                    d.append(txt[_]+txt[_+1])
                    _+=2
                    
            else:
                d.append(txt[_])
                    #d.append(v[_+1])
                _+=1
    
    if txt != d:
        d = ENCODE(d , vocab)
    return d

def DECODE(X,vocab):
    S = ""
    for i in X:
        S+=vocab[i]
    return S
    

#print(len(s))
S = time.time()
#print(ENCODE(s,vocab))
#print(VOCAB)
s = [VOCAB[i] for i in ENCODE(s,vocab)]
print(s)
E = time.time()-S
#print(s)
#print(E)
print(DECODE(s,vocab))