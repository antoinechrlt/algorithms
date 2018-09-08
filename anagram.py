# -*- coding: utf-8 -*-
import unittest

class Anagram():

	@staticmethod
	def groupAnagram(string):
		"""
			Given a string of words, group words which are anagram between them

			:param string: String of words to group by anagram
			:type string: str
			:return res: Array of set of anagram in the string
			:rtype: obj<list>
		"""

		n_mots = list(set(string.split()))
		mydic = {}
		for mot in n_mots:
			key = "".join(sorted(mot))
			if key in mydic:
					mydic[key].append(mot)
			else:
				mydic[key] = [mot]
		res = []
		for key in mydic:
			if len(mydic[key]) > 1:
				res.append({mot for mot in mydic[key]})
		return res


class TestAnagram(unittest.TestCase):

	def testGroupAnagram(self):
		string = "le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme"
		# [{"marche","charme"},{"chine","chien","niche"},{"limace","malice"},{"une","nue"}]
		self.assertEqual(len(Anagram.groupAnagram(string)),4)

if __name__ == "__main__":
	unittest.main()