package io.powersecurity;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.crypto.password.PasswordEncoder;

import io.powersecurity.models.User;
import io.powersecurity.repository.UserRepository;

@SpringBootApplication
public class PowerSecurityServerApplication implements CommandLineRunner{

	@Autowired
	private UserRepository userRepository;
	
	@Autowired
	private PasswordEncoder passwordEncoder;
	
	public static void main(String[] args) {
		SpringApplication.run(PowerSecurityServerApplication.class, args);
	}
	
	@Override
	public void run(String... args) throws Exception {
		List<User> users = userRepository.findAll();
		if(users.size() == 0) {
			User user = new User("admin", passwordEncoder.encode("admin123"), "ADMIN");
			userRepository.save(user);
		}
	}

}
