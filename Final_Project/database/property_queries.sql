drop TABLE VIC;
drop TABLE Listings;
drop TABLE PostcodeLGA;
drop TABLE LGA_ID;


CREATE TABLE LGA_ID (
	lga_desc VARCHAR,
	lga_ID FLOAT,
PRIMARY KEY (lga_ID)	
	);
	
SELECT * FROM LGA_ID;


CREATE TABLE PostcodeLGA (
domain_id FLOAT, 
suburb VARCHAR,
postcode FLOAT,
lat FLOAT,
lng FLOAT,
lga_id FLOAT,
PRIMARY KEY (Domain_id),	
FOREIGN KEY (lga_id) REFERENCES LGA_ID (lga_id)	
);

SELECT * FROM postcodeLGA;

CREATE TABLE VIC (
Domain_id FLOAT ,
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
Domain_id FLOAT,	
streetNumber VARCHAR,        
streetName VARCHAR,          
streetType VARCHAR,           
geoLocation VARCHAR,           
propertyType VARCHAR,         
bedrooms FLOAT,             
bathrooms FLOAT,             
carspaces FLOAT,                
propertyDetailsUrl  VARCHAR,     
price FLOAT,                 
unitNumber VARCHAR,           
second_ID VARCHAR,               
canonicalUrl  VARCHAR,           
areaSize FLOAT,                  
photos  VARCHAR,
FOREIGN KEY (Domain_id) REFERENCES PostcodeLGA (Domain_id)	
	);
	
SELECT * FROM Listings;



