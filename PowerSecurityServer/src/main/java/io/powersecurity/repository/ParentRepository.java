package io.powersecurity.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.Parent;

@Repository
public interface ParentRepository extends JpaRepository<Parent, Long>{

}
