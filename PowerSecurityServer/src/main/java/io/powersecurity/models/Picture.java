package io.powersecurity.models;

import java.io.IOException;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import org.springframework.web.multipart.MultipartFile;

import com.sun.jdi.InvalidTypeException;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name="pictures")
@NoArgsConstructor
@AllArgsConstructor
@Data
public class Picture {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;
	
	@Lob
	private byte[] picture;
	
	private String fileName;
	
	
	@ManyToOne(cascade = {CascadeType.DETACH,CascadeType.REFRESH})
	private Entry person;
	
	public void setMultipartFile(MultipartFile file,String type) throws IOException,InvalidTypeException {
		this.picture = file.getBytes();
		this.fileName = this.picture.hashCode() + ".jpg";

	}
	
}
