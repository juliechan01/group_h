package com.codingdojo.yiip.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseStatus;

import com.codingdojo.yiip.models.Business;
import com.codingdojo.yiip.services.BusinessService;

@Controller
public class BusinessController {

	@Autowired
	private BusinessService businessService;

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@GetMapping("/api/business")
	public ResponseEntity<List<Business>> getAllBusinesses() {
		return new ResponseEntity<>(businessService.getAllBusinesses(), HttpStatus.OK);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@GetMapping("/api/business/{id}")
	public ResponseEntity<Business> getOneGame(@PathVariable("id") Long id) {
		return new ResponseEntity<>(businessService.getOneBusinessById(id), HttpStatus.OK);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.CREATED)
	@PostMapping("/api/business")
	public ResponseEntity<Business> createBusiness(@RequestBody Business business) {
		return new ResponseEntity<>(businessService.createBusiness(business), HttpStatus.CREATED);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@PutMapping("/api/business/{id}")
	public ResponseEntity<Business> updateBusiness(@RequestBody Business editedBusiness) {
		return new ResponseEntity<>(businessService.updateBusiness(editedBusiness), HttpStatus.OK);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@DeleteMapping("/api/business/{id}")
	public ResponseEntity<String> deleteGame(@PathVariable("id") Long id) {
		businessService.deleteBusiness(id);
		return new ResponseEntity<>("Game Deleted", HttpStatus.OK);
	}
}
