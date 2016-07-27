
def char2alpha(char):
    if char == 'あ':
        return 'a'
    if char == 'い':
        return 'i'
    if char == 'う':
        return 'u'
    if char == 'え':
        return 'e'
    if char == 'お':
        return 'o'
    if char == 'か' or char == 'き' or char == 'く' or char == 'け' or char == 'こ':
        return 'k'
    if char == 'が' or char == 'ぎ' or char == 'ぐ' or char == 'げ' or char == 'ご':
        return 'g'
    if char == 'さ' or char == 'し' or char == 'す' or char == 'せ' or char == 'そ':
        return 's'
    if char == 'ざ' or char == 'じ' or char == 'ず' or char == 'ぜ' or char == 'ぞ':
        return 'z'
    if char == 'た' or char == 'ち' or char == 'つ' or char == 'て' or char == 'と':
        return 't'
    if char == 'だ' or char == 'ぢ' or char == 'づ' or char == 'で' or char == 'ど':
        return 'd'
    if char == 'な' or char == 'に' or char == 'ぬ' or char == 'ね' or char == 'の' or char == 'ん':
        return 'n'
    if char == 'は' or char == 'ひ' or char == 'ふ' or char == 'へ' or char == 'ほ':
        return 'h'
    if char == 'ば' or char == 'び' or char == 'ぶ' or char == 'べ' or char == 'ぼ':
        return 'b'
    if char == 'ぱ' or char == 'ぴ' or char == 'ぷ' or char == 'ぺ' or char == 'ぽ':
        return 'p'
    if char == 'ま' or char == 'み' or char == 'む' or char == 'め' or char == 'も':
        return 'm'
    if char == 'や' or char == 'ゆ' or char == 'よ':
        return 'y'
    if char == 'ら' or char == 'り' or char == 'る' or char == 'れ' or char == 'ろ':
        return 'r'
    if char == 'わ' or char == 'を':
        return 'w'
    return 0

def hira2alpha(text):
    text = text.strip()
    chars = text.strip('')
    alphas = ''
    for char in chars:
        alpha = char2alpha(char)
        alphas = alphas + alpha
    return alphas

text = 'わたなべ'

print(hira2alpha(text))
