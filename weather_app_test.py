import pytest
from unittest.mock import patch, MagicMock
import weather_app
import socket
import ntplib


def test_Weather_success():
    """Test Weather function with successful API response"""
    with patch('weather_app.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.text = "Weather data for Tehran"
        mock_get.return_value = mock_response
        
        # Capture print output
        with patch('builtins.print') as mock_print:
            weather_app.Weather("Tehran")
            
            # Check if requests.get was called with correct URL
            mock_get.assert_called_once_with("https://wttr.in/Tehran")
            # Check if weather data was printed
            mock_print.assert_any_call("Weather data for Tehran")
            # Check if MyGithub was called
            mock_print.assert_any_call("        +======================+")
            mock_print.assert_any_call("        |    !G I T H U B!     |")


def test_Weather_exception():
    """Test Weather function when request fails"""
    with patch('weather_app.requests.get') as mock_get:
        mock_get.side_effect = Exception("Network error")
        
        with patch('builtins.print') as mock_print:
            weather_app.Weather("UnknownCity")
            
            mock_print.assert_called_with("🌐 Please connect to the internet to use this application!")


def test_check_internet_success():
    """Test check_internet when connection is successful"""
    with patch('socket.socket') as mock_socket:
        mock_socket.return_value.__enter__.return_value.connect.return_value = None
        result = weather_app.check_internet()
        assert result == True


def test_check_internet_failure():
    """Test check_internet when connection fails"""
    with patch('socket.socket') as mock_socket:
        mock_socket.return_value.__enter__.return_value.connect.side_effect = socket.error
        result = weather_app.check_internet()
        assert result == False


def test_get_internet_time_success():
    """Test get_internet_time with successful NTP response"""
    with patch('weather_app.ntplib.NTPClient') as mock_client:
        mock_response = MagicMock()
        mock_response.tx_time = 1609459200  # Fixed timestamp
        mock_client.return_value.request.return_value = mock_response
        
        with patch('weather_app.ctime') as mock_ctime:
            mock_ctime.return_value = "Fri Jan  1 00:00:00 2021"
            
            with patch('builtins.print') as mock_print:
                weather_app.get_internet_time()
                
                mock_print.assert_called_with("                      🕓 Date : ", "Fri Jan  1 00:00:00 2021")


def test_get_internet_time_exception():
    """Test get_internet_time when NTP request fails"""
    with patch('weather_app.ntplib.NTPClient') as mock_client:
        mock_client.return_value.request.side_effect = Exception("NTP error")
        
        with patch('builtins.print') as mock_print:
            weather_app.get_internet_time()
            
            # Should not print anything on exception
            mock_print.assert_not_called()


def test_MyGithub_without_param():
    """Test MyGithub function without parameter"""
    with patch('weather_app.get_internet_time') as mock_time:
        with patch('builtins.print') as mock_print:
            weather_app.MyGithub()
            
            mock_time.assert_called_once()
            # Check if the main banner is printed
            mock_print.assert_any_call("                   |----------[⛅ Weather App ⛅]----------|")


def test_MyGithub_with_true():
    """Test MyGithub function with True parameter"""
    with patch('builtins.print') as mock_print:
        weather_app.MyGithub(True)
        
        # Should print GitHub ASCII art
        mock_print.assert_any_call("        +======================+")
        mock_print.assert_any_call("        |    !G I T H U B!     |")
        mock_print.assert_any_call("        |     ID: ADKO1396     |")


def test_help():
    """Test help function"""
    with patch('builtins.print') as mock_print:
        weather_app.help()
        
        # Should print help information
        mock_print.assert_any_call("⭕ To see the weather in your city, simply type its name and you'll be able to view the forecast. \n")
        mock_print.assert_any_call("📃 |=> To view the list of countries, type the 'countries' command. \n")


def test_Start():
    """Test Start function"""
    with patch('builtins.print') as mock_print:
        weather_app.Start()
        
        # Should print welcome message
        mock_print.assert_any_call("🖤 Hello, welcome to the weather app! If you like this app, please follow my GitHub. Thank you! For guidance. \n")
        mock_print.assert_any_call("🛑 you can use the help command \n")


def test_City_Help():
    """Test City_Help function"""
    with patch('builtins.print') as mock_print:
        weather_app.City_Help()
        
        # Should print city help information
        mock_print.assert_any_call("🌄 To view the cities of your country, type : \city_help. \n")
        mock_print.assert_any_call("💻 Type : \city_help \n")


def test_get_country_function_success():
    """Test get_country_function with existing country"""
    with patch('builtins.input', return_value='Iran'):
        with patch('builtins.print') as mock_print:
            with patch('countries.CountryName_All_V4') as mock_v4:
                result = weather_app.get_country_function()
                
                # Should call the country function
                mock_v4.assert_called_once_with('Iran')
                assert result is None  # Since we're mocking the function


def test_get_country_function_not_found():
    """Test get_country_function with non-existing country"""
    with patch('builtins.input', return_value='UnknownCountry'):
        with patch('builtins.print') as mock_print:
            result = weather_app.get_country_function()
            
            # Should print error message
            mock_print.assert_called_with("❌ Function for country 'UnknownCountry' not found!")
            assert result is None


def test_main_with_internet():
    """Test main function when internet is available"""
    with patch('weather_app.check_internet', return_value=True):
        with patch('weather_app.MyGithub') as mock_github:
            with patch('weather_app.Start') as mock_start:
                with patch('weather_app.Value_User') as mock_value:
                    weather_app.main()
                    
                    mock_github.assert_called_once()
                    mock_start.assert_called_once()
                    mock_value.assert_called_once()


def test_main_without_internet():
    """Test main function when no internet connection"""
    with patch('weather_app.check_internet', return_value=False):
        with patch('builtins.print') as mock_print:
            weather_app.main()
            
            mock_print.assert_called_with("🌐 Please connect to the internet to use this application! ")


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
