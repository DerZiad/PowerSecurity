package io.powersecurity.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.powersecurity.models.Picture;

@Repository
public interface PictureRepository extends JpaRepository<Picture, Long> {

}
