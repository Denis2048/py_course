"""Программа для чтения *.xml файла и конвертации градусов Цельсия в градусы Фаренгейта"""
import xml.etree.ElementTree as ET


class TemperatureConverter:
    """Метод класса для конвертации"""
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0 / 5.0 * temperature_in_celsius + 32


class ForecastXmlParser:
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter

    def parse(self, file):
        """Метод для парсинга данных и преобразования"""
        with open(file, 'r') as fo:
            tree = ET.parse(fo)
            root = tree.getroot()
            for child in root:
                temperature_in_celsius = int(child.find("temperature_in_celsius").text)
                temperature_in_fahrenheit = round(self.temperature_converter.convert_celsius_to_fahrenheit(temperature_in_celsius), 1)
                print(f"{child.find("day").text}: {temperature_in_celsius} ℃, convert: {temperature_in_fahrenheit} ℉")
