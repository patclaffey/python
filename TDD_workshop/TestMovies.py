import unittest
import MyMovies

class TestMovies(unittest.TestCase):

    def setUp(self):
        pass


    def setTearDown(self):
        pass


    def test_find_year_in_line(self):

        test_harness = (
                ('Jaws (1975)', '1975'),
                ('Starwars 1977)', '1977'),
                ('2001 A Space Odyssey ( 1968 )', '1968'),
                ('Back to the future 1985.', '1985'),
                ('Raiders of the lost ark 1981 .', '1981'),
                ('jurassic park 1993', '1993'),
                ('The Matrix 1999', '1999'),
                ('A fist full of Dollars', None),
                ('10,000 BC (2008)', '2008'),
                ('1941 (1979)', '1979'),
                ('24 Hour Party People (2002)', '2002'),
                ('300 (2007)', '2007'),
                ('2010', None)
                )
        for line, expected in test_harness:
            film = MyMovies.Movies()
            result = film.find_year_in_line(line)
            self.assertEqual(expected,result, msg='Year error  ' + line )

    def test_find_movie_in_line(self):

        test_harness = (
                ('Jaws (1975)', 'Jaws'),
                ('Starwars 1977)', 'Starwars'),
                ('2001 A Space Odyssey ( 1968 )', '2001 A Space Odyssey'),
                ('Back to the future 1985.', 'Back to the future'),
                ('Raiders of the lost ark 1981 .', 'Raiders of the lost ark'),
                ('jurassic park 1993', 'jurassic park'),
                ('The Matrix 1999', 'The Matrix'),
                ('A fist full of Dollars', 'A fist full of Dollars'),
                ('10,000 BC (2008)', '10,000 BC'),
                ('1941 (1979)', '1941'),
                ('24 Hour Party People (2002)', '24 Hour Party People'),
                ('300 (2007)', '300'),
                ('2010', '2010')
                )
        for line, expected in test_harness:
            film = MyMovies.Movies()
            result = film.find_film_in_line(line)
            self.assertEqual(expected,result, msg='Movie error  ' + line )


    def test_find_decade(self):

        test_harness = (
                ('1968','1960s'),            
                ('1975','1970s'),
                ('1977','1970s'),
                ('1979','1970s'),
                ('1985','1980s'),
                ('1981','1980s'),
                ('1993','1990s'),
                ('1999','1990s'),
                (None,None),
                ('2008','2000s'),
                ('2002','2000s'),
                ('2007','2000s'),
                )
        for line, expected in test_harness:
            film = MyMovies.Movies()
            result = film.find_decade(line)
            self.assertEqual(expected,result, msg='Decade error  ' + repr(line) )


    def test_get_decade_total(self):

        test_data = (
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
        
        expected = {
            '1960s':1 ,
            '1970s':3 ,
            '1980s':2 ,
            '1990s':2 ,
            '2000s':3 
            }
        
        film = MyMovies.Movies()
        result = film.get_decade_totals(test_data)
        self.assertEqual(expected,result, msg='Error summarizing data  ' )


    def test_print_decade_totals(self):


        test_data = {
            '1960s':1 ,
            '1970s':3 ,
            '1980s':2 ,
            '1990s':2 ,
            '2000s':3 
            }
        
        film = MyMovies.Movies()
        result = film.print_decade_totals(test_data)
        expected = True
        self.assertEqual(expected,result, msg='Error printing data  ' )
        

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest( TestMovies('test_find_year_in_line' ) )
    suite.addTest( TestMovies('test_find_movie_in_line' ) )
    suite.addTest( TestMovies('test_find_decade' ) )
    suite.addTest( TestMovies('test_get_decade_total' ) )
    suite.addTest( TestMovies('test_print_decade_totals' ) )
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
        
