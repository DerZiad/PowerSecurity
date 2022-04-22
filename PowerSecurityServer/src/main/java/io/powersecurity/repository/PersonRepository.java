package io.powersecurity.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.Person;

@Repository
public interface PersonRepository extends JpaRepository<Person, String>{

}
