package io.powersecurity.services.implementations;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Primary;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import io.powersecurity.exceptions.DangerousException;
import io.powersecurity.exceptions.NoDataFoundException;
import io.powersecurity.exceptions.StrangerException;
import io.powersecurity.models.Entry;
import io.powersecurity.repository.PersonRepository;
import io.powersecurity.services.EntriesService;

@Service
@Primary
public class EntriesServiceImplementation implements EntriesService{

	@Autowired
	private PersonRepository personRepository;
	
	public Page<Entry> getEntries(int pagenumber) throws NoDataFoundException{
		/*Page<Entry> datas = personRepository.findAll(Page);
		if(datas.isEmpty()) throw new NoDataFoundException("No data found");
		return datas;*/
		return null;
	}

	@Override
	public void validateEntry(Entry entry) throws StrangerException, DangerousException {
		if(entry.isCompleted()) {
			//Search algorithm
		}else {
			throw new StrangerException();
		}
		
	}


}
