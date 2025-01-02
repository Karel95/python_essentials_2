from sys import path

path.append('../modules')
path.append('../packages')
# path.append('../packages/extrapack.zip')

import module # type: ignore
import extra.iota # type: ignore
import extra.good.best.sigma as sig # type: ignore
import extra.good.alpha as alp  # type: ignore
 
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

print(extra.iota.FunI())
print(sig.FunS())
print(alp.FunA())
