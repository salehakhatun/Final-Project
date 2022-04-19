drop TABLE Victoria;
drop TABLE Listings;
drop TABLE LGA_ID;
drop TABLE postcodeLGA;

CREATE TABLE Victoria (
Suburb VARCHAR(25),
Postcode INT,
Lat  FLOAT,
Lng  FLOAT,
Domain_id INT,
medianSoldPrice FLOAT,
numberSold  FLOAT,
highestSoldPrice   FLOAT,        
lowestSoldPrice    FLOAT,         
medianSaleListingPrice     FLOAT, 
numberSaleListing     FLOAT,      
highestSaleListingPrice    FLOAT, 
lowestSaleListingPrice    FLOAT,  
auctionNumberAuctioned    FLOAT,   
auctionNumberSold        FLOAT,    
auctionNumberWithdrawn   FLOAT,     
daysOnMarket             FLOAT,    
medianRentListingPrice    FLOAT,   
numberRentListing          FLOAT, 
highestRentListingPrice     FLOAT,
lowestRentListingPrice      FLOAT
);
	
SELECT * FROM Victoria;

CREATE TABLE Listings (
streetNumber VARCHAR,         
streetName VARCHAR,          
streetType VARCHAR,           
suburb VARCHAR,               
postcode FLOAT,           
state VARCHAR(3),                 
geoLocation VARCHAR,           
propertyType VARCHAR,         
bedrooms INT,             
bathrooms FLOAT,             
carspaces FLOAT,                
result  VARCHAR,               
agent VARCHAR,                   
id INT,                     
agencyId INT,               
agencyName  VARCHAR,            
agencyProfilePageUrl  VARCHAR,   
propertyDetailsUrl  VARCHAR,     
price INT,                 
unitNumber VARCHAR,           
area INT,                    
second_ID VARCHAR,               
canonicalUrl  VARCHAR,           
areaSize INT,                  
photos  VARCHAR
	);
	
SELECT * FROM Listings;

CREATE TABLE LGA_ID (
	lga_desc VARCHAR,
	lga_ID INT
	);
	
SELECT * FROM LGA_ID;

CREATE TABLE postcodeLGA (
postcode INT,
LGA VARCHAR
);

SELECT * FROM postcodeLGA;
