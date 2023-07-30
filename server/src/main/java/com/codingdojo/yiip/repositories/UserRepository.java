package com.codingdojo.yiip.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.codingdojo.yiip.models.User;

public interface UserRepository extends JpaRepository<User, Long>{
	Optional<User> findByEmail(String email);
}
