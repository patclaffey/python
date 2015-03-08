import re

class Movies(object):


    def __init__(self):
        pass


    def find_year_in_line(self, line):
        
        pat = re.compile('\S+\s+\S*(\d{4})[\s).]*$' )

        if pat.search(line):
            year = pat.search(line).group(1)
        else:
            year = None
            
        return year

    
    def find_film_in_line(self, line):
        
        pat = re.compile('[\s]+[\s(]*\d{4}[\s).]*$' )
        
        mysplit = pat.split( line )
        film_name = mysplit[0]

        if not re.search('\S+', film_name):
            film_name = None
        
        return film_name

    
    def find_decade(self, year_in):
        
        if year_in == None:
            year = 0
        else:
            year = int(year_in)


        if year >= 1960 and year <= 1969:
            decade = '1960s'
        elif year >= 1970 and year <= 1979:
            decade = '1970s'
        elif year >= 1980 and year <= 1989:
            decade = '1980s'
        elif year >= 1990 and year <= 1999:
            decade = '1990s'
        elif year >= 2000 and year <= 2009:
            decade = '2000s'
        else:
            decade = None
            
        return decade


    def get_decade_totals(self, data_in):
        hold_results =      {'1960s':0,
                            '1970s':0,
                            '1980s':0,
                            '1990s':0,
                            '2000s':0}
        for line in data_in:
            year = self.find_year_in_line(line)
            decade = self.find_decade(year)
            if decade != None:
                hold_results[ decade] = hold_results[ decade] + 1
                
        return hold_results


    def print_decade_totals(self, data_in):
        print("")
        for k,v in sorted(data_in.items()):
            print (k + ': ' + str(v)  )
        
        return True


if __name__ == '__main__':
    movie_data = (
                'Jaws (1975)',
                'Starwars 1977)', 
                '2001 A Space Odyssey ( 1968 )', 
                'Back to the future 1985.',
                'Raiders of the lost ark 1981 .',
                'jurassic park 1993',
                'The Matrix 1999', 
                'A fist full of Dollars', 
                '10,000 BC (2008)',
                '1941 (1979)', 
                '24 Hour Party People (2002)',
                '300 (2007)', 
                '2010'
                )
    film = Movies()
    result = film.get_decade_totals(movie_data)
    print_output = film.print_decade_totals(result)

