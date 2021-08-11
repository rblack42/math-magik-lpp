from mmdesigner.Covering import Covering


def main():
	cov = Covering('scad/covering_data.json')
	cov.run()

if __name__ == '__main__':
	main()
