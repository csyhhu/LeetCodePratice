class Codec:

    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        encode_url = hash(longUrl)
        self.encode_map[longUrl] = encode_url
        self.decode_map[encode_url] = longUrl
        
        return encode_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """

        return self.decode_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = 'https://leetcode.com/problems/design-tinyurl'
print(codec.decode(codec.encode(url)))