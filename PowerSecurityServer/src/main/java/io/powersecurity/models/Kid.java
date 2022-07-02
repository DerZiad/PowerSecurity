package io.powersecurity.models;

import javax.persistence.CascadeType;
import javax.persistence.DiscriminatorColumn;
import javax.persistence.Entity;
import javax.persistence.ManyToOne;

@Entity
@DiscriminatorColumn(name = "k",columnDefinition = "kid")
public class Kid extends Person {

	@ManyToOne(cascade = { CascadeType.DETACH, CascadeType.REFRESH }, targetEntity = Parent.class)
	private Parent parent;

	public Kid(Long id, PersonalInformation personalInformations, User user, Parent parent) {
		super(id, personalInformations, user);
		this.parent = parent;
	}

	public Parent getParent() {
		return parent;
	}

	public void setParent(Parent parent) {
		this.parent = parent;
	}

}
