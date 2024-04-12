#!/usr/bin/env python3

from typing import Dict

class PrefixMapSum:
	""" """

	_map: Dict[str, int]

	def __init__(self) -> None:
		""" """
		self._map = dict()
	
	def insert(self, key: str, value: int) -> None:
		""" O(1) runtime"""
		self._map[key] = value

	def sum(self, prefix: str) -> int:
		""" Return the sum of all values of keys that begin with a given prefix. 
  		O(n) runtime
    	"""
		total = 0
		for key in self._map.keys():
			if key.startswith(prefix):
				total += self._map[key]
		return total


def main():
    mapsum = PrefixMapSum()
    mapsum.insert("columnar", 3)
    mapsum.insert("column", 2)
    mapsum.insert("co", 4)
    mapsum.insert("c", 2)
    mapsum.insert("coi", 1)
    print(f"mapsum.sum('col') = {mapsum.sum('col')}")
    print(f"mapsum.sum('column') = {mapsum.sum('column')}")
    print(f"mapsum.sum('co') = {mapsum.sum('co')}")
    print(f"mapsum.sum('c') = {mapsum.sum('c')}")
    print(f"mapsum.sum('a') = {mapsum.sum('a')}")

if __name__ == "__main__":
	main()
