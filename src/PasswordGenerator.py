#!/usr/bin/python
# coding: utf-8

import os
import sys
reload(sys).setdefaultencoding("utf-8")

def main():
	
	return




if __name__ == '__main__':
	core = getattr(sys.modules["__main__"], "__file__", None)
	if core:
		root = os.path.dirname(os.path.abspath(core))
		if root:
			os.chdir(root)
	main()
