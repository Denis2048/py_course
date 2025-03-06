from temp_conv import TemperatureConverter, ForecastXmlParser


if __name__ == "__main__":
    temperature_converter = TemperatureConverter()
    forecast_xml_parser = ForecastXmlParser(temperature_converter)
    forecast_xml_parser.parse("forecast.xml")
