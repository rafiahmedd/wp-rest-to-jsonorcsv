import requests
from bs4 import BeautifulSoup
from CsvWriter import CsvWriter
from JsonWriter import JsonWriter

class Driver():
    Driver = None;
    def __init__(self):
        self.Driver = None;
        self.data = [];
        self.filename = "fluent_answers.csv";
        self.file = None;
        self.writer = None;
        self.queryPage = 1;
        self.perPage = 100;
        self.totalPages = 0;
        self.is_running_first_time = True;

        
    # Prepare data for writing
    def prepareData(self, data, type):
        dataList = dict() if type == "json" else list()
        for dataKey, dataValue in enumerate(data):
                title = BeautifulSoup(dataValue["title"]["rendered"], features="html.parser").get_text().replace("\n", '');
                content = BeautifulSoup(dataValue["content"]["rendered"], features="html.parser").get_text().replace("\n", '');
                excerpt = BeautifulSoup(dataValue["excerpt"]["rendered"], features="html.parser").get_text().replace("\n", '');
                link = dataValue["link"];
                if (type == "json"):
                    dataList[dataKey] = {
                        "title": title,
                        "content": content,
                        "link": link,
                        "excerpt": excerpt
                    }
                else:
                    dataList.append([title, title, content, excerpt]);
        return dataList;

    # Request data from the API
    def requestData(self, url):
        url = f"{url}?page={self.queryPage}&per_page={self.perPage}";
        try:
            response = requests.get(url);
            self.data = response.json();
            if self.is_running_first_time:
                self.totalPages = response.headers['X-Wp-Totalpages'];
                self.is_running_first_time = False;
            if len(self.data)-1 == self.perPage:
                self.queryPage += 1
        except:
            print("Error: Something went wrong while requesting data");
            return False;

    # Write data to file
    def writeData(self, type="csv"):
        self.data = self.prepareData(self.data, type);
        driver = type.capitalize()+"Writer"
        self.Driver = eval(driver)
        self.Driver(self.filename).write(self.data);
       
        self.queryPage += 1;
    
    def fileName(self, type):
        return f"fluent_answers_{self.queryPage}.{type}";

    def startWriting(self, url, type="csv"):
        if (self.totalPages == 0):
           self.requestData(url); 
        while (int(self.queryPage) <= int(self.totalPages)):
            print(f"Getting data from page {self.queryPage}");
            self.filename = self.fileName(type);
            self.requestData(url);
            self.writeData(type);
        print("Done!");