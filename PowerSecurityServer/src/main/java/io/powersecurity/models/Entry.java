package io.powersecurity.models;

import java.sql.Date;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import io.powersecurity.models.enums.PersonState;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "persons")
@AllArgsConstructor
@NoArgsConstructor
@Data
public class Entry {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;

	private String firstName;

	private String lastName;

	private String kidFirstName;

	private String kidLastName;

	private Date currentConnexion = new Date(System.currentTimeMillis());

	private boolean completed = false;

	private String password;
	
	@Enumerated(EnumType.STRING)
	private PersonState personState;

	@OneToMany(cascade = CascadeType.ALL, mappedBy = "person")
	private List<Picture> pictures = new ArrayList<>();

}
