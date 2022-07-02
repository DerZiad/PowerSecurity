package io.powersecurity.models;

import java.sql.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;

import lombok.NoArgsConstructor;

import lombok.AllArgsConstructor;

@Entity
@Table(name="personalinformations")
@AllArgsConstructor
@NoArgsConstructor
@Data
public class PersonalInformation {
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;
	private String identityCardNumber;
	private String firstName;
	private String lastName;
	private Date birthday;
	
}
