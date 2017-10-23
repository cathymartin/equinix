
class Island():

	def __init__(self):
		'''define roman to numeric hash'''
		self.symbol_dict={'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}

	def symboltranslate(self, s):
		''' translate roman to numeric'''
		
		total = 0
		#print total
		for i in xrange(0, len(s) - 1):
			if self.symbol_dict[s[i]] < self.symbol_dict[s[i+1]]:
				total -= self.symbol_dict[s[i]]
			else:
				total += self.symbol_dict[s[i]]
		total += self.symbol_dict[s[-1]]
		
		return total 

	def processinput(self, ifile):
		'''ifile is a text file with input lines, process line by line'''

		f = open(ifile, 'r')
		sum=0
		tmpkey=''
		for line in f:
			#print self.symbol_dict
			linesplit=line.strip().split(' ')
			#print linesplit

			if linesplit[1]=='is' and linesplit[2] in self.symbol_dict.keys():
				#newstring mapping to roman char, add to hash
				self.symbol_dict[linesplit[0]]=linesplit[2]
			elif linesplit[-1]=='Credits':
				#assuming credits are Silver, Gold, Iron. Translate to numeric and add to hash
				sum=int(linesplit[-2])
				for k in xrange(len(linesplit)-3):
					#print linesplit[k]
					if linesplit[k] in self.symbol_dict.keys() and self.symbol_dict[linesplit[k]].isdigit():
						sum -= self.symbol_dict[linesplit[k]]
					elif linesplit[k] in self.symbol_dict.keys() and str(self.symbol_dict[self.symbol_dict[linesplit[k]]]).isdigit():
						sum -= self.symbol_dict[self.symbol_dict[linesplit[k]]]
					elif linesplit[k] in ['Silver','Gold','Iron']:
						self.symbol_dict[linesplit[k]]=sum

			elif linesplit[0]=='how' and linesplit[1]=='much' and linesplit[2]=='is':
				#process qustion with string map to roman char to num, print outline
				roman=''
				outline=''
				for m in xrange(3, len(linesplit)-1):
					roman += self.symbol_dict[linesplit[m]]
					outline += linesplit[m]+' '
				#print roman
				outline += 'is '
				outline += str(self.symboltranslate(roman))
				print outline

			elif linesplit[0]=='how' and linesplit[1]=='many':
				#process question with Credits, also use current hash
				roman=''
				outline=''
				sum=0
				for m in xrange(4, len(linesplit)-1):
					#print linesplit[m]
					if linesplit[m] not in ['Silver','Gold','Iron']:
						roman += self.symbol_dict[linesplit[m]]
						outline += linesplit[m]+' '
					elif linesplit[m] in ['Silver','Gold','Iron']:
						#print roman
						#print outline
						#print linesplit[m]
						sum=self.symboltranslate(roman)+self.symbol_dict[linesplit[m]]
						outline += linesplit[m]
				outline += ' is '
				outline += str(sum)
				print outline

			else:
				print 'I have no idea what you are talking about'

		f.close()

		return


myisland=Island()

myisland.processinput('island_input.txt')










