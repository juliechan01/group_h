package com.codingdojo.yiip.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.codingdojo.yiip.models.Business;
import com.codingdojo.yiip.repositories.BusinessRepository;

@Service
public class BusinessService {

	@Autowired
	private BusinessRepository businessRepo;
	
	public Business createBusiness(Business business) {
		return businessRepo.save(business);
	}
	
	public List<Business> getAllBusinesses(){
		return businessRepo.findAll();
	}
	
	public Business getOneBusinessById(Long id) {
		Optional<Business> possibleBusiness = businessRepo.findById(id);
		
		if (possibleBusiness.isPresent()) {
			return possibleBusiness.get();
		}
		
		return null;
	}
	
	public Business updateBusiness(Business business) {
		return businessRepo.save(business);
	}
	
	public void deleteBusiness(Long id) {
		businessRepo.deleteById(id);
	}
}
