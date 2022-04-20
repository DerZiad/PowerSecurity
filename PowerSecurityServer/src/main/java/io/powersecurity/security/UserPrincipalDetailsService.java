package io.powersecurity.security;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import io.powersecurity.models.User;
import io.powersecurity.repository.UserRepository;

@Service
public class UserPrincipalDetailsService implements UserDetailsService {
	@Autowired
	private UserRepository userRepository;

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
		User user = this.userRepository.findById(username)
				.orElseThrow(() -> new UsernameNotFoundException("Username or password are invalid"));
		return user;
	}
}