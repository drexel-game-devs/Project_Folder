import java.util.*;
import java.io.*;
import java.net.*;
import com.google.gson.*;

//Lab 01
//Matthew Freihofer
//Joseph Lipinski

public class Lab_1 
{
	public static void main(String[] args) throws Exception
	{
		//create a scanner object
		Scanner scan = new Scanner(System.in);
		
		//reference to key, and the string URL
		String key, sURL;
		
		//get the key from the user
		if(args.length < 1)
		{
			System.out.print("Enter key: ");
			key = scan.nextLine();
		}	
		else
			key = args[0];
		
		//close the scanner
		scan.close();
		
		//create the HTTP string
		sURL = "http://api.wunderground.com/api/" + key + "/conditions/hourly/q/19104.json";
		
		//Connect to the URL
		URL url = new URL(sURL);
		HttpURLConnection request = (HttpURLConnection) url.openConnection();
		request.connect();
		
		//JSON Parser parses JSON text
		//JsonElement stores data being requested in an object
		//JsonObject stores that data inside JsonElement so it can be manipulated
		JsonParser jp = new JsonParser();
		JsonElement root = jp.parse(new InputStreamReader((InputStream) request.getContent()));
		JsonObject rootObj = root.getAsJsonObject();
		
		//store JsonObject as Array for later
		JsonArray JsonArray = rootObj.get("hourly_forecast").getAsJsonArray();
		
		//pull the zip code down and print it
		int Zip = rootObj.get("current_observation").getAsJsonObject().get("display_location").getAsJsonObject().get("zip").getAsInt();
		System.out.println("Zip: " + Zip + "\n");
		
		//Gather data for the next few days
		for(int i = 0; i < JsonArray.size(); i++)
		{			
			//Get the Month, Day, Year, Time
			String dateTime = rootObj.get("hourly_forecast").getAsJsonArray().get(i).getAsJsonObject().get("FCTTIME").getAsJsonObject().get("pretty").getAsString();
			System.out.println("Current Date and Time: " + dateTime);
		
			//Get the current conditions
			String condition = rootObj.get("hourly_forecast").getAsJsonArray().get(i).getAsJsonObject().get("condition").getAsString();
			System.out.println("Condition: " + condition);
		
			//Get the current temperature
			String temperature = rootObj.get("hourly_forecast").getAsJsonArray().get(i).getAsJsonObject().get("temp").getAsJsonObject().get("english").getAsString();
			System.out.println("Temperature: " + temperature + "F");
		
			//Get the humidity
			String humidity = rootObj.get("hourly_forecast").getAsJsonArray().get(i).getAsJsonObject().get("humidity").getAsString();
			System.out.println("Humidity: " + humidity + "%");
			
			//Formatting
			System.out.println();
			System.out.println();
		}
	}
}
