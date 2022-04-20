package io.powersecurity.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.User;

@Repository
public interface UserRepository extends JpaRepository<User, String>{

}
