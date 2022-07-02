package io.powersecurity.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.Kid;

@Repository
public interface KidRepository extends JpaRepository<Kid, Long>{

}
