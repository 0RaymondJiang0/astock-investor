import random
import codecs

class RandomChar():
  """用于随机生成汉字对应的Unicode字符"""
  @staticmethod
  def Unicode():
    val = random.randint(0x4E00, 0x9FBB)
    return unichr(val)

  @staticmethod
  def GB2312():
    head = random.randint(0xB0, 0xCF)
    body = random.randint(0xA, 0xF)
    tail = random.randint(0, 0xF)
    val = ( head << 8 ) | (body << 4) | tail
    str = "%x" % val

    decode_hex = codecs.getdecoder("hex_codec")

    # return str
    # print(str.__class__)
    # return str
    #
    # return str.encode('gb2312').decode('hex')#.decode('gb2312','ignore')
    # return str.encode('gb2312').decode('gb2312', 'ignore')#.decode('gb2312','ignore')
    return decode_hex(str)[0].decode('gb2312', 'ignore')