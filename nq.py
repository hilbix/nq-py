#
# ZeroMQ based NQ
#

import sys
import zmq

class nq(object):

	def __init__(self, url=None):
		self._ctx	= zmq.Context()
		self._url	= None
		self._sock	= None
		if url:
			self.bind(url)

	def bind(self, url=None):
		if url:
			self._url	= url
			if self._sock:
				
		return self._url

	def add(self, q, data):
		pass

def main(argv):
	pass

if __name__=='__main__':
	main(sys.argv)

