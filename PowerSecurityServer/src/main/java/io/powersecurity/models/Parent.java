package io.powersecurity.models;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.DiscriminatorColumn;
import javax.persistence.Entity;
import javax.persistence.OneToMany;

@Entity
@DiscriminatorColumn(name = "p",columnDefinition = "parent")
public class Parent extends Person {

	@OneToMany(cascade = CascadeType.ALL,mappedBy = "parent")
	private List<Kid> kids = new ArrayList<Kid>();

	public Parent(Long id, PersonalInformation personalInformations, User user, List<Kid> kids) {
		super(id, personalInformations, user);
		this.kids = kids;
	}

	public List<Kid> getKids() {
		return kids;
	}

	public void setKids(List<Kid> kids) {
		this.kids = kids;
	}

}
