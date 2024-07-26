import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
//import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.remote.DesiredCapabilities;

public class SeleniumDemo {
	public static void main(String[] args) {
		//System.setProperty("webdriver.geck.driver", "./geckodriver");
		//DesiredCapabilities capabilities = DesiredCapabilities.firefox();
		//capabilities.setCapability("marionette", true);
		WebDriver driver = new FirefoxDriver();
		//WebDriver driver = new ChromeDriver(); // For chrome
		driver.get("https://www.facebook.com/");
		driver.manage().window().maximize();
		driver.findElement(By.name("email")).sendKeys("abcd");
		driver.findElement(By.name("pass")).sendKeys("abcd");
		//driver.quit();
	}
}
