package io.powersecurity.services;

import org.springframework.data.domain.Page;

import io.powersecurity.exceptions.DangerousException;
import io.powersecurity.exceptions.NoDataFoundException;
import io.powersecurity.exceptions.StrangerException;
import io.powersecurity.models.Entry;


public interface EntriesService {

	public Page<Entry> getEntries(int pagenumber) throws NoDataFoundException;
	
	public void validateEntry(Entry entry) throws StrangerException,DangerousException;
}
