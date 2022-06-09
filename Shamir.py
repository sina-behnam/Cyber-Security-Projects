from fractions import Fraction
from utils import *

def print_reconstructor(shares,X=2,is_fraction=True):
	print('\n<<<<<< The Calculation of shares are: >>>>>>\n')

	for j, share_j in enumerate(shares):    ## -> share_j = (x, y)
		xj, yj = share_j

		print(yj,'*',end=' ')
		for i, share_i in enumerate(shares):
			xi, _ = share_i

			e_ch = '*'
			if i == len(shares)-1: 
				e_ch = ''

			if i != j:
				print('( {} - {} )/( {} - {} )'.format(X,xi,xj,xi),end=' {} '.format(e_ch))
		print('+')

	print('\n---------------------------------\n')

	if is_fraction:
		print('The Fraction of above equassion !!! \n')

		for j, share_j in enumerate(shares):    ## -> share_j = (x, y)
			xj, yj = share_j
			print(yj,'* (',end=' ')
			for i, share_i in enumerate(shares):
				xi, _ = share_i

				e_ch = '*'
				if i == len(shares)-1: 
					e_ch = ''

				if i != j:
					print(Fraction((X-xi),(xj-xi)),end=' {} '.format(e_ch))
			if j != len(shares)-1:
				print(') +',end=' ')
			else:
				print(')')
	print('\n---------------------------------\n')


def reconstruct_share(shares,X=2,module=23):
	
	sums = 0
	for j, share_j in enumerate(shares):    ## -> share_j = (x, y)
		xj, yj = share_j
		prod = 1
		for i, share_i in enumerate(shares):
			xi, _ = share_i
			if i != j:
				d_f = (X-xi)/(xj-xi)
				prod *= d_f

		prod *= yj
		sums += prod

	fr_result = Fraction(sums).limit_denominator()

	print("The simplified result is : ",fr_result)
		
	d = fr_result.denominator%module
	n = fr_result.numerator%module

	return (module_inverse(d,module) * n)%module

def reconstruct_secret(shares,module=23):
	sums = 0
	for j, share_j in enumerate(shares):    ## -> share_j = (x, y)
		xj, yj = share_j
		prod = 1
		for i, share_i in enumerate(shares):
			xi, _ = share_i
			if i != j:
				d_f = (xi)/(xj-xi)
				prod *= d_f

		prod *= yj
		sums += prod

	fr_result = Fraction(sums).limit_denominator()

	print("The simplified result for our secret is: ",fr_result)
		
	d = fr_result.denominator%module
	n = fr_result.numerator%module

	return (module_inverse(d,module) * n)%module


def argument_parser():
	"""
	Argument parser for the Shamir's Secret Sharing Scheme.
	"""
	import argparse
	parser = argparse.ArgumentParser(description='Shamir Secret Sharing Scheme')
	parser.add_argument('-x', '--share', type=int, default=2, help='The person share number')
	parser.add_argument('-m', '--module', type=int, default=23, help='Module value')
	parser.add_argument('-f', '--fraction', action='store_true', help='Print the fraction of the equation')
	parser.add_argument('-p', '--print', action='store_true', help='Print the shares')
	parser.add_argument('-s', '--secret', action='store_true', help='Reconstruct the secret')
	return parser.parse_args()

# Driver code
if __name__ == '__main__':
	args = argument_parser()
	t, n = 4,6
	S = [(1,3), (3,9), (4,13), (6,21)]
	if args.print:
		print_reconstructor(S,args.share,args.fraction)
	
	print("\n")
	print("The share of person {}  is : ".format(args.share),reconstruct_share(S,args.share,args.module))
	print("\n")
	if args.secret:
		print("The Secret is : ",reconstruct_secret(S,args.module))


