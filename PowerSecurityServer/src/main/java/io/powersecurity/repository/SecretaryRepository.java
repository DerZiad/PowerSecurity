package io.powersecurity.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.Secretary;

@Repository
public interface SecretaryRepository extends JpaRepository<Secretary, Long>{

}
