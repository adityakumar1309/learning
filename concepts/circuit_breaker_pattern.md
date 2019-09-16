## Circuit Breaker Pattern

Learn how the circuit breaker pattern ensures stable performance in your microservices by monitoring for failures and providing an alternate service or error message.

Software systems make remote calls to software running in different processes, usually on different machines across a network. One of the big differences between in-memory calls and remote calls is that remote calls can fail, or hang without a response until some timeout limit is reached. What's worse, if you have many callers on an unresponsive supplier, you can run out of critical resources leading to cascading failures across multiple systems.

Solution
The circuit breaker pattern is the solution to this problem. The basic idea behind the circuit breaker is very simple. 

## You wrap a protected function call in a circuit breaker object, which monitors for failures. 

## Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return with an error or with some alternative service or default message, without the protected call being made at all. 

## This will make sure system is responsive and threads are not waiting for an unresponsive call.

Different States of the Circuit Breaker

The circuit breaker has three distinct states: Closed, Open, and Half-Open:

Closed – When everything is normal, the circuit breaker remains in the closed state and all calls pass through to the services. When the number of failures exceeds a predetermined threshold the breaker trips, and it goes into the Open state.

Open – The circuit breaker returns an error for calls without executing the function.

Half-Open – After a timeout period, the circuit switches to a half-open state to test if the underlying problem still exists. If a single call fails in this half-open state, the breaker is once again tripped. If it succeeds, the circuit breaker resets back to the normal, closed state. 

Example

You can implement the circuit breaker pattern with Netflix Hystrix. The following code can better explain the solution. 

The below microservice recommends the reading list to the customer:

package hello;

import org.springframework.boot.SpringApplication;

import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.web.bind.annotation.RestController;

import org.springframework.web.bind.annotation.RequestMapping;

@RestController

@SpringBootApplication

public class BookstoreApplication {

@RequestMapping(value = "/recommended")

public String readingList(){

return "Spring in Action (Manning), Cloud Native Java (O'Reilly), Learning Spring Boot (Packt)";

}

public static void main(String[] args) {

SpringApplication.run(BookstoreApplication.class, args);

}

}


Client application code which will call the reading list recommendation service:

package hello;

import java.net.URI;

import org.springframework.stereotype.Service;

import org.springframework.web.client.RestTemplate;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;

@Service

public class BookService {

  private final RestTemplate restTemplate;

  public BookService(RestTemplate rest) {

  this.restTemplate = rest;

}

@HystrixCommand(fallbackMethod = "reliable")

public String readingList() {

  URI uri = URI.create("http://localhost:8090/recommended");

  return this.restTemplate.getForObject(uri, String.class);

}

public String reliable() {

  return "Cloud Native Java (O'Reilly)";

}

}


In the above code method, the reading list is calling remote microservice API to get the reading list recommendation. Look at line number 19 of the above code, we have provided fallback method "reliable." If the remote API does not respond in time, the method "reliable" will be called and that will serve the request.

In the fallback method, you can return either a default output or even call some other remote or local API to serve the request.
