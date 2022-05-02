drop TABLE VIC;
drop TABLE Listings;
drop TABLE LGA_ID;
drop TABLE PostcodeLGA;

CREATE TABLE LGA_ID (
	lga_desc VARCHAR,
	lga_ID INT,
PRIMARY KEY (lga_ID)	
	);
	
SELECT * FROM LGA_ID;


CREATE TABLE PostcodeLGA (
domain_id INT, 
suburb VARCHAR,
postcode INT,
lat FLOAT,
lng FLOAT,
lga_id INT,
PRIMARY KEY (Domain_id),	
FOREIGN KEY (lga_id) REFERENCES LGA_ID (lga_id)	
);

SELECT * FROM postcodeLGA;

CREATE TABLE VIC (
Domain_id INT ,
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
lowestRentListingPrice      FLOAT,
FOREIGN KEY (Domain_id) REFERENCES PostcodeLGA (Domain_id)	
);
	
SELECT * FROM VIC;

CREATE TABLE Listings (
Domain_id INT,	
streetNumber VARCHAR,        
streetName VARCHAR,          
streetType VARCHAR,           
geoLocation VARCHAR,           
propertyType VARCHAR,         
bedrooms INT,             
bathrooms FLOAT,             
carspaces FLOAT,                
propertyDetailsUrl  VARCHAR,     
price FLOAT,                 
unitNumber VARCHAR,           
second_ID VARCHAR,               
canonicalUrl  VARCHAR,           
areaSize INT,                  
photos  VARCHAR,
FOREIGN KEY (Domain_id) REFERENCES PostcodeLGA (Domain_id)	
	);
	
SELECT * FROM Listings;



