package io.powersecurity.repository;


import java.util.List;

import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.Picture;

import org.springframework.boot.autoconfigure.domain.EntityScan;



@Repository
public interface PictureRepository extends JpaRepository<Picture,Integer>{
	
	

}
