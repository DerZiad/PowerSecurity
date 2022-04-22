package io.powersecurity;

import java.io.InputStreamReader;
import java.util.Collection;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.Persistence;
import javax.persistence.Query;

import org.hibernate.Session;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.boot.autoconfigure.domain.EntityScan;

import io.powersecurity.models.*;
import io.powersecurity.repository.*;

@EntityScan("io.powersecurity.models")
@SpringBootApplication
public class PowerSecurityServerApplication implements CommandLineRunner {

	public EntityManager em;

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
		if (users.size() == 0) {
			User user = new User("admin", passwordEncoder.encode("admin123"), "ADMIN");
			userRepository.save(user);

		}

	}

}
